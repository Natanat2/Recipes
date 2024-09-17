import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";
import Categories from "./Categories";

const CategoryDetail = () => {
  const { id } = useParams();
  const [category, setCategory] = useState(null);

  useEffect(() => {
    axios
      .get(`/api/categories/${id}/`)
      .then((response) => setCategory(response.data))
      .catch((error) => console.error(error));
  }, [id]);

  if (!category) return <div>Loading...</div>;

  return (
    <div>
      <Categories />
      <h1>{category.name}</h1>
      <p>{category.descriptionCategory}</p>
      <h2>Рецепты:</h2>
      <ul>
        {category.recipes.map((recipe) => (
          <li key={recipe.id}>
            <Link to={`/recipes/${recipe.id}/`}>{recipe.nameRecipe}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryDetail;
