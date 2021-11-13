import React from 'react';
import { useState, useEffect } from 'react';

//API
import API from '../../API';

//Config
import { POSTER_SIZE, BACKDROP_SIZE, IMAGE_BASE_URL } from '../../config';

//Components

//Hooks

//Images
import NoImage from '../../images/no_image.jpg';


const Home = () => {

  const [state, setState] = useState();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  const fetchMovies = async (page, searchTerm) => {
    
    try {
      setError(false);
      setLoading(true);
      
      const movies = await API.fetchMovies(searchTerm, page);
      console.log('Movies from API');
      console.log(movies);

      setState((prev) => ({
        ...movies,
        results:
          page > 1 ? [...prev.results, ...movies.results] : [...movies.results]
      }));
    }
    catch (error) {
      setError(true);
    }
    setLoading(false);

  };

  //Initial Render
  //Fetch movies from first page
  //Emtpy dependency array [] means it runs once on mount
  //ie when the component loads for the first time
  useEffect(() => {
    fetchMovies(1);
  }, []);

  console.log('Printing State');
  console.log(state);

  return <div>Home Page</div>
};

export default Home;
