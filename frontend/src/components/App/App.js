import React, { useState } from "react";
import Main from "../Main/Main";
import "./App.css";
import Filters from "../Filters/Filters";
import { DataProvider } from "../Filters/components/DataContext/DataContext";
import Header from "../Header/Header";

function App() {
    const [coordinatesPoint, setCoordinatesPoint] = useState({ lng: 37.4155, lat: 55.7022 }) // const [coordinatesPoint, setCoordinatesPoint] = useState(null)
    const [selectedCrossingFilters, setSelectedCrossingFilters] = useState(null)
    const [filterNames, setFilterNames] = useState({})

  return (
    <DataProvider>
      <div className="app">
        <Header />
        <Filters coordinatesPoint={coordinatesPoint} setSelectedCrossingFilters={setSelectedCrossingFilters} setFilterNames={setFilterNames}/>
        <Main setCoordinatesPoint={setCoordinatesPoint} selectedCrossingFilters={selectedCrossingFilters} filterNames={filterNames}/>
      </div>
    </DataProvider>
  );
}

export default App;
