import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';

import "./Filter.css";
import {useFormik} from "formik";
import { AddressesField } from "./components/AddressesField/AddressesField"
import useFetch from "../../hooks/useFetch";
import {useMemo, useState, useEffect, useRef} from "react";
import {CadastralsField} from "./components/CadastralField/CadastralField";
import {AreaField} from "./components/AreaField/AreaField";
import {DistrictField} from "./components/DistrictField/DistrictField";
import { getOptionsAndMap, getFilterOptions, formatCrossingFilters} from "./utils";
import {FieldNames} from "./constant";
import { useData } from './components/DataContext/DataContext';

 function Filters() {
    const { setTestData } = useData()
    const [localData, setLocalData] = useState(null)

    const [submitCode, setSubmitCode] = useState(null);
    const areas = useFetch('http://178.20.44.143:8080/navigation/filters/areas');
    const addresses = useFetch('http://178.20.44.143:8080/navigation/filters/addresses');
    const cadastrals = useFetch('http://178.20.44.143:8080/navigation/filters/cadastrals');
    const districts = useFetch('http://178.20.44.143:8080/navigation/filters/districts');
    const crossingFilters = useFetch('http://178.20.44.143:8080/crossing/filters/')
    
    const areasData = useMemo(() => getOptionsAndMap(areas), [areas]);
    const districtData = useMemo(() => getOptionsAndMap(districts), [districts]);
    const addressesData = useMemo(() => getOptionsAndMap(addresses), [addresses]);
    const cadastralData = useMemo(() => getOptionsAndMap(cadastrals), [cadastrals]);
    const crossingFiltersData = useMemo(() => getFilterOptions(crossingFilters), [crossingFilters]);
    console.log(crossingFiltersData)

    const [filterValues, setFilterValues] = useState({});
    const [showToolTip, setShowToolTip] = useState(null);
    const refSetTimeout = useRef();

    const onMouseEnterHandler = (option) => {
        refSetTimeout.current = setTimeout(() => {
          setShowToolTip(option);
        }, 750);
      };
    
      const onMouseLeaveHandler = () => {
        clearTimeout(refSetTimeout.current);
        setShowToolTip(null);
      };

    const sendPostRequest = async () => {
        try {
            const res = await fetch('http://178.20.44.143:8080/polygons/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: submitCode,
            });
            if (!res.ok) {
                throw new Error('Response is not ok')
            }
            const data = await res.json()
            console.log(data)
            setLocalData(data)
        } catch (error) {
            console.error('Error: ', error)
        }
    }
    
    const formik = useFormik({
        initialValues: {
            [FieldNames.areas]: [],
            [FieldNames.addresses]: [],
            [FieldNames.cadastrals]: [],
            [FieldNames.districts]: [],
            [FieldNames.crossingFilters]: {},
        },
        onSubmit: (values) => {
            setSubmitCode(JSON.stringify(values));
        }
    });

    useEffect(() => {
        if (submitCode) {
            sendPostRequest(submitCode)
        }
    }, [submitCode])

    useEffect(() => {
        setTestData(localData)
    }, [localData])

    const handleCheckboxChange = (option, isChecked) => {
        setFilterValues(prevValues => ({
          ...prevValues,
          [option]: {
            isChecked,
            value: isChecked ? 0 : null
          }
        }));
    };

    const handleRadioChange = (option, key, newValue) => {
        setFilterValues(prevValues => ({
          ...prevValues,
          [option]: {
            ...prevValues[option],
            value: newValue
          }
        }));
        formik.setFieldValue(`crossingFilters.${key}`, newValue)
      };

    const card = (
        <React.Fragment>
            <form onSubmit={formik.handleSubmit}>
                <Box className="form-container">
                    <label htmlFor="addresses">Поиск по адресу</label>
                    <AddressesField
                        value={formik.values.addresses}
                        onChange={(_, newValue) =>
                            formik.setFieldValue(FieldNames.addresses, newValue)
                        }
                        loading={addresses.loading}
                        addresses={addressesData.map}
                        options={addressesData.options}
                    />
                    <label htmlFor="cadastrals">Поиск по кадастру</label>
                    <CadastralsField
                        value={formik.values.cadastrals}
                        onChange={(_, newValue) =>
                            formik.setFieldValue(FieldNames.cadastrals, newValue)
                        }
                        loading={cadastrals.loading}
                        cadastrals={cadastralData.map}
                        options={cadastralData.options}
                    />
                    <label htmlFor="areas">Поиск по округам</label>
                    <AreaField
                        values={formik.values.areas}
                        onChange={(_, newValue) => {
                            formik.setFieldValue(FieldNames.areas, newValue)
                        }}
                        options={areasData.options}
                        loading={areas.loading}
                        areas={areasData.map}
                    />
                    <label htmlFor="areas">Поиск по районам</label>
                    <DistrictField
                        values={formik.values.districts}
                        onChange={(_, newValue) => {
                            formik.setFieldValue(FieldNames.districts, newValue)
                        }}
                        options={districtData.options}
                        loading={districts.loading}
                        areas={districtData.map}
                    />

                    <div>
                        {crossingFiltersData.options.map(option => {
                            const { description, key } = crossingFiltersData.map.get(option);
                            const isChecked = filterValues[option]?.isChecked || false;
                            const radioValue = filterValues[option]?.value;
                            return (
                                <div>
                                    <label>
                                        {option}
                                        <sup onMouseEnter={() => onMouseEnterHandler(option)} onMouseLeave={onMouseLeaveHandler}>?</sup>
                                        <input
                                            type="checkbox"
                                            onChange={(e) => handleCheckboxChange(option, key, e.target.checked)}
                                            checked={isChecked}
                                        />
                                        <div className="tooltip">
                                            {showToolTip &&
                                                <div className="tooltiptext">{description}</div>
                                            }
                                        </div>
                                    </label>
                                    {isChecked &&
                                        <div>
                                            <div>
                                                <label>Строгое исключение
                                                    <input 
                                                        type="radio"
                                                        name={option}
                                                        value={0}    
                                                        checked={radioValue === 0}
                                                        onChange={() => handleRadioChange(option, 0)}
                                                    />
                                                </label>
                                            </div>
                                            <div>
                                                <label>Допустимое пересечение
                                                    <input 
                                                        type="radio"
                                                        name={option}
                                                        value={1}    
                                                        checked={radioValue  === 1}
                                                        onChange={() => handleRadioChange(option, 1)}
                                                    />
                                                </label>
                                            </div>
                                            <div>
                                                <label>Отсутствие влияния
                                                    <input 
                                                        type="radio"
                                                        name={option}
                                                        value={2}    
                                                        checked={radioValue === 2}
                                                        onChange={() => handleRadioChange(option, 2)}
                                                    />
                                                </label>
                                            </div>
                                        </div>
                                    }
                                </div>
                            );
                        })}
                    </div>
                    
                    <button type="submit">Submit</button>
                </Box>
            </form>
        </React.Fragment>
    );

    return (
        <Box className="filters">
            <Card className="filters-card" variant="outlined">{card}</Card>
        </Box>
    );
}
export default Filters;