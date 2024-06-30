import React from 'react';
import profile from '../../images/header/profile_icon.png'
import './Header.css'

const Header = () => {
    return (
        <div className='header__container'>
            <div className='pages'>
                <p>Анализ территорий</p>
                <p>Избранное</p>
                <p>История поиска</p>
            </div>
            <div className='profile'>
                <p>Иванов В.П.</p>
                <img src={profile} alt="profile icon" />
            </div>
        </div>
    );
};

export default Header;