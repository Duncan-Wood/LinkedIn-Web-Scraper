// firebaseConfig.js
import { initializeApp } from 'firebase/app';

const firebaseConfig = {
    apiKey: "AIzaSyAwzpBkeCseGzXw-MYhM5mOyT-d2xN2jAc",
    authDomain: "linkedin-job-helper.firebaseapp.com",
    projectId: "linkedin-job-helper",
    storageBucket: "linkedin-job-helper.appspot.com",
    messagingSenderId: "90927315007",
    appId: "1:90927315007:web:791a35324f563ac29be08a",
    measurementId: "G-VW45P471FX"
};

const firebaseApp = initializeApp(firebaseConfig);

export default firebaseApp;
