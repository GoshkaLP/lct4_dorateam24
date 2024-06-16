import React from "react";
import Counter from "../Counter/Counter";
import FilterList from "../FilterList/FilterList";
import "./Header.css";

function Header({data, onChangeFilter, quantity }) {
    return (
        <header className="header">
            <Counter quantity={quantity} />
            <FilterList data={data} onChangeFilter={onChangeFilter}/>
            <button className="header__button" type="submit">Применить фильтры</button>
        </header>
    );
}

export default Header;