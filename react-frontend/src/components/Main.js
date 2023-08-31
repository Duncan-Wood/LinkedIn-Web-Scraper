import { Route, Routes } from "react-router-dom";

export default function Main() {
  return (
    <>
      <Routes>
        <Route path="/" exact component={Home} />
        {/* Add more routes as needed */}
      </Routes> 
    </>
  );
}
