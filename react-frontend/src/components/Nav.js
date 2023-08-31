import React from "react";
import { Link } from "react-router-dom";

const Nav = () => {
  return (
    <header>
      <h1>LinkedIn Job helper</h1>
      <ul>
        <li>
          <Link to="/">Home</Link>
          <Link to="/login">Login</Link>
        </li>
      </ul>
    </header>
  );
};

export default Nav;
