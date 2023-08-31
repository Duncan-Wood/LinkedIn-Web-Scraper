import "./App.css";
import Nav from "./components/Nav";
import Home from "./components/Home";


const App = () => {
  return (
    <>
      <Nav id='nav'/>
      <main id='main'>
        <Home id='home'/>
      </main>
    </> 
    );
};

export default App;
