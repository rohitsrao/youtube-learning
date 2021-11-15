import React from 'react';
import { useParams } from 'react-router-dom';

//Config
import { IMAGE_BASE_URL, POSTER_SIZE } from '../../config';

//Components
import Actor from '../Actor';
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
      <Grid header='Actors'>
        {movie.actors.map(actor => (
          <Actor
            key={actor.credit_id}
            name={actor.name}
            character={actor.character}
            imageUrl={
              actor.profile_path
                ? `${IMAGE_BASE_URL}${POSTER_SIZE}${actor.profile_path}`  
                : NoImage
            }
          />
        ))}
      </Grid>
    </>
  );

};

export default Movie;
