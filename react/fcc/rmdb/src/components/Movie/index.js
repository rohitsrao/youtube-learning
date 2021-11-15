import React from 'react';
import { useParams } from 'react-router-dom';

//Config
import { IMAGE_BASE_URL, POSTER_SIZE } from '../../config';

//Components
import BreadCrumb from '../BreadCrumb';
import Grid from '../Grid';
import MovieInfo from '../MovieInfo';
import MovieInfoBar from '../MovieInfoBar';
import Spinner from '../Spinner';

//Hook
import { useMovieFetch } from '../../hooks/useMovieFetch';

//Image
import NoImage from '../../images/no_image.jpg';

const Movie = () => {

  const { movieId } = useParams();
  const { state: movie, loading, error } = useMovieFetch(movieId);

  if (error) return <div>Something went wrong ...</div>;
  if (loading) return <Spinner />;

  return (
    <>
      <BreadCrumb movieTitle={movie.original_title} />
      <MovieInfo movie={movie} />
      <MovieInfoBar
        time={movie.runtime}
        budget={movie.budget}
        revenue={movie.revenue}
      />
    </>
  );

};

export default Movie;
