import React, { useState } from "react";
import Main from "../Main/Main";
import "./App.css";
import Filters from "../Filters/Filters";
import { DataProvider } from "../Filters/components/DataContext/DataContext";

function App() {
    const [coordinatesPoint, setCoordinatesPoint] = useState(null)
    const [selectedCrossingFilters, setSelectedCrossingFilters] = useState(null)
    const [filterNames, setFilterNames] = useState({})

  return (
    <DataProvider>
      <div className="app">
        <Filters coordinatesPoint={coordinatesPoint} setSelectedCrossingFilters={setSelectedCrossingFilters} setFilterNames={setFilterNames}/>
        <Main setCoordinatesPoint={setCoordinatesPoint} selectedCrossingFilters={selectedCrossingFilters} filterNames={filterNames}/>
      </div>
    </DataProvider>
  );
}

export default App;
