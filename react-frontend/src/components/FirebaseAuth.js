// ./components/FirebaseAuth.js
import { getAuth, onAuthStateChanged, signOut, createUserWithEmailAndPassword, signInWithEmailAndPassword, connectAuthEmulator } from 'firebase/auth';
import firebaseApp from '../firebaseConfig';

const auth = getAuth(firebaseApp);
// must start the firebase server with:
// firebase serve --only hosting
// then start the firebase emulator with:
// firebase emulators:start --only auth
connectAuthEmulator(auth, "http://localhost:9099");

export {
  auth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  onAuthStateChanged,
  signOut
};
