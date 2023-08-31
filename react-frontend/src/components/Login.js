// ./components/Login.js
import { useState } from 'react';
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from './FirebaseAuth';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      await signInWithEmailAndPassword(email, password);
    } catch (error) {
      console.log(`There was an error: ${error}`);
      // Handle login error
    }
  };

  const handleSignup = async () => {
    try {
      await createUserWithEmailAndPassword(email, password);
    } catch (error) {
      console.log(`There was an error: ${error}`);
      // Handle signup error
    }
  };

  return (
    <div>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleSignup}>Signup</button>
    </div>
  );
};

export default LoginForm;
