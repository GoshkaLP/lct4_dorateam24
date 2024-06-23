import React, { useState } from "react";
import Main from "../Main/Main";
import "./App.css";
import Filters from "../Filters/Filters";
import { DataProvider } from "../Filters/components/DataContext/DataContext";

function App() {
    const [coordinatesPoint, setCoordinatesPoint] = useState(null)

  return (
    <DataProvider>
      <div className="app">
        <Filters coordinatesPoint={coordinatesPoint}/>
        <Main setCoordinatesPoint={setCoordinatesPoint}/>
      </div>
    </DataProvider>
  );
}

export default App;
