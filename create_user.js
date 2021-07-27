db = db.getSiblingDB('admin');
db.createUser(
  {
    user: "gateway-api",
    pwd: "123ladybug123",
    roles: [
        {
            role: "readWrite",
            db: "gateway-api"
        }
    ],
    mechanisms: [
        "SCRAM-SHA-1"
    ]
  }
);