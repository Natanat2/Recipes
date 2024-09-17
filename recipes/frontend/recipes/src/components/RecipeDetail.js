import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import Categories from "./Categories";

const RecipeDetail = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    axios
      .get(`/api/recipes/${id}/`)
      .then((response) => setRecipe(response.data))
      .catch((error) => console.error(error));
  }, [id]);

  if (!recipe) return <div>Loading...</div>;

  return (
    <div>
      <Categories />
      <h1>{recipe.nameRecipe}</h1>
      <img src={recipe.image} alt={recipe.nameRecipe} />
      <p>{recipe.description}</p>
      <h2>Ingredients</h2>
      <p>{recipe.products}</p>
      <h2>Steps</h2>
      <p>{recipe.steps}</p>
    </div>
  );
};

export default RecipeDetail;
