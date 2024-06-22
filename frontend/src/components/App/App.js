import React from "react";
import Main from "../Main/Main";
import "./App.css";
import Filters from "../Filters/Filters";

function App() {

  return (
    <div className="app">
      <Filters />
      <Main data={[]} polygons={[]} hexbin={[]} />
    </div>
  );
}

export default App;
