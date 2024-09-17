import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

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
      <h1>{category.name}</h1>
      <p>{category.descriptionCategory}</p>
    </div>
  );
};

export default CategoryDetail;
