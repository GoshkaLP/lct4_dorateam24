import React, { useState } from "react";
import { MultiSelect } from "react-multi-select-component";
import "./Filter.css";

function Filter(props) {
  const { name, options, onChangeFilter, fieldName } = props;
  const [selected, setSelected] = useState([]);

  const handleChange = (values) => {
      setSelected(values);
      onChangeFilter(fieldName, values.map(item => item.value));
  }

  const customValueRenderer = (selected, _options) => {
    return selected.length
    ? `Выбрано ${selected.length}`
    : "Не выбрано";
  };

  return (
    <li className="filter">
      <p className="filter-name">{ name }</p>
      {/* <pre>{JSON.stringify(selected)}</pre> */}
        <MultiSelect
          className="filter-multiselect"
          options={options}
          value={selected}
          onChange={handleChange}
          labelledBy={"Select"}
          isCreatable={true}
          overrideStrings={{
              "allItemsAreSelected": "Выбраны все",
              "clearSearch": "Очистить поиск",
              "clearSelected": "Очистить выбранные",
              "noOptions": "Нет вариантов:(",
              "search": "Поиск",
              "selectAll": "Выбрать все",
              "selectAllFiltered": "Выбрать все (отфильтрованы)",
              "selectSomeItems": "Выбрать...",
              "create": "Создать",
          }}
          valueRenderer={customValueRenderer}
        />
    </li>
  );
}

export default Filter;
