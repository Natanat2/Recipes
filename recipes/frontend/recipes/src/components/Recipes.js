import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const Recipes = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    axios
      .get("/api/recipes/")
      .then((response) => setRecipes(response.data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Рецепты</h1>
      <ul>
        {recipes.map((recipe) => (
          <li key={recipe.id}>
            <Link to={`/recipes/${recipe.id}`}>{recipe.nameRecipe}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recipes;
