from datetime import datetime
from app.models import Log


def test_read_logs(client, db_session):
    log1 = Log(
        source="auth-service",
        message="Logged in",
        level="INFO",
        timestamp=datetime.utcnow(),
    )
    log2 = Log(
        source="payment",
        message="Payment failed",
        level="ERROR",
        timestamp=datetime.utcnow(),
    )
    db_session.add_all([log1, log2])
    db_session.commit()

    response = client.get("/logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2
