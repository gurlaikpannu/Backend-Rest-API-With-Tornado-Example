def getUser(db, userId):
  db.get("users", { "id": userId })
