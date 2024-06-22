import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';

import "./Filter.css";
import {useFormik} from "formik";
import { AddressesField } from "./components/AddressesField/AddressesField"
import useFetch from "../../hooks/useFetch";
import {useMemo, useState} from "react";
import {CadastralsField} from "./components/CadastralField/CadastralField";
import {AreaField} from "./components/AreaField/AreaField";
import {DistrictField} from "./components/DistrictField/DistrictField";
import { getOptionsAndMap} from "./utils";
import {FieldNames} from "./constant";

export default function Filters() {
    const [submitCode, setSubmitCode] = useState("");
    const areas = useFetch('http://178.20.44.143:8080/layers/areas');
    const addresses = useFetch('http://178.20.44.143:8080/layers/addresses');
    const cadastrals = useFetch('http://178.20.44.143:8080/layers/cadastrals');
    const districts = useFetch('http://178.20.44.143:8080/layers/districts');
    const areasData = useMemo(() => getOptionsAndMap(areas), [areas]);
    const districtData = useMemo(() => getOptionsAndMap(districts), [districts]);
    const addressesData = useMemo(() => getOptionsAndMap(addresses), [addresses]);
    const cadastralData = useMemo(() => getOptionsAndMap(cadastrals), [cadastrals]);

    const formik = useFormik({
        initialValues: {
            [FieldNames.areas]: [],
            [FieldNames.addresses]: [],
            [FieldNames.cadastrals]: [],
            [FieldNames.districts]: [],
        },
        onSubmit: (values) => {
            console.log(values);
            setSubmitCode(JSON.stringify(values));
        }
    });

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
