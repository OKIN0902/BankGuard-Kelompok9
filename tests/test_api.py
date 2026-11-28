from pathlib import Path
import pytest
from werkzeug.security import generate_password_hash
from backend.app import create_app

TX = dict(user_id="USER-001",amount=10000000,historical_average=500000,destination_new=True,transfers_10min=1)

@pytest.fixture
def app(tmp_path):
    return create_app(dict(TESTING=True,SECRET_KEY="test-only-not-production",
                           BANKGUARD_DEMO_USER="petugas",
                           BANKGUARD_DEMO_PASSWORD_HASH=generate_password_hash("test-password",method="pbkdf2:sha256:1000"),
                           BANKGUARD_DB_PATH=str(tmp_path/"test.db"),INSTANCE_NAME="BankGuard-Test"))

def token(client):
    return client.get("/api/session").get_json()["csrf_token"]

def post(client,url,data,csrf):
    return client.post(url,json=data,headers={"X-CSRF-Token":csrf})

def login(client):
    return post(client,"/api/login",dict(username="petugas",password="test-password"),token(client))

def test_health_session(app):
    c=app.test_client()
    assert c.get("/api/health").get_json()=={"status":"ok","instance":"BankGuard-Test"}
    res=c.get("/api/session")
    assert res.get_json()["authenticated"] is False
    assert "HttpOnly" in res.headers["Set-Cookie"] and "SameSite=Lax" in res.headers["Set-Cookie"]
    assert c.get("/api/transactions").status_code==401

def test_login_csrf_logout(app):
    c=app.test_client()
    old=token(c)
    assert post(c,"/api/login",{},"wrong").status_code==403
    assert post(c,"/api/login",dict(username="petugas",password="wrong"),old).status_code==401
    assert c.post("/api/login",data="x",headers={"X-CSRF-Token":old}).status_code==415
    res=post(c,"/api/login",dict(username="petugas",password="test-password"),old)
    assert res.status_code==200
    new=res.get_json()["csrf_token"]
    assert new!=old
    assert post(c,"/api/transactions",TX,old).status_code==403
    assert post(c,"/api/logout",{},new).get_json()["authenticated"] is False
    assert c.get("/api/transactions").status_code==401

def test_transaction_and_restart(app):
    c=app.test_client()
    csrf=login(c).get_json()["csrf_token"]
    res=post(c,"/api/transactions",{**TX,"score":0},csrf)
    assert res.status_code==201
    tx=res.get_json()["transaction"]
    assert tx["score"]==75 and tx["level"]=="TINGGI" and tx["destination_new"] is True
    assert len(tx["id"])==36 and tx["created_at"].endswith("Z")
    summary=c.get("/api/transactions").get_json()
    assert summary["total"]==summary["high_count"]==1
    assert summary["low_count"]==summary["medium_count"]==0
    assert summary["transactions"]==[tx]
    restarted=create_app(dict(app.config))
    c2=restarted.test_client()
    login(c2)
    assert c2.get("/api/transactions").get_json()["transactions"]==[tx]

@pytest.mark.parametrize("change",[{"amount":True},{"amount":"100"},{"amount":0},{"historical_average":0},
 {"destination_new":1},{"transfers_10min":1.0},{"user_id":""},{"user_id":"x"*65}])
def test_invalid(app,change):
    c=app.test_client()
    csrf=login(c).get_json()["csrf_token"]
    assert post(c,"/api/transactions",{**TX,**change},csrf).status_code==400
    assert c.get("/api/transactions").get_json()["total"]==0

def test_missing_field_and_invalid_json(app):
    c=app.test_client()
    csrf=login(c).get_json()["csrf_token"]
    assert post(c,"/api/transactions",{},csrf).status_code==400
    assert c.post("/api/transactions",data="{",content_type="application/json",headers={"X-CSRF-Token":csrf}).status_code==400

def test_database_unavailable(app):
    path=Path(app.config["BANKGUARD_DB_PATH"])
    path.unlink()
    assert app.test_client().get("/api/health").status_code==503

def test_missing_secret(app):
    with pytest.raises(RuntimeError):
        create_app({**app.config,"SECRET_KEY":None})
