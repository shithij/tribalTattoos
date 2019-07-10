import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("tribal-tattoo-ae837-firebase-adminsdk-em2bs-c5b3a1bd5a.json")
defaultApp = firebase_admin.initialize_app(cred)
db = firestore.client()

docs = db.collection(u'events').get()
print(docs)
# for doc in docs:
#     print(doc.id)