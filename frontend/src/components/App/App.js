import React, { useState } from "react";
import Main from "../Main/Main";
import "./App.css";
import Filters from "../Filters/Filters";
import { DataProvider } from "../Filters/components/DataContext/DataContext";

function App() {


  return (
    <DataProvider>
      <div className="app">
        <Filters />
        <Main />
      </div>
    </DataProvider>
  );
}

export default App;
