import React from 'react';
import { Link } from 'react-router-dom';

import RMDBLogo from '../../images/react-movie-logo.svg';
import TMDBLogo from '../../images/tmdb_logo.svg';

import { Wrapper, Content, RMDBLogoImg, TMDBLogoImg } from './Header.styles';

const Header = () => (
  <Wrapper>
    <Content>
      <Link to='/'>
        <RMDBLogoImg src={RMDBLogo} alt='rmdb-logo'/>
      </Link>
      <TMDBLogoImg src={TMDBLogo} alt='tmdb-logo'/>
    </Content>
  </Wrapper>
);

export default Header;
