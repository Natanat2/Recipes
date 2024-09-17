import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Сайт с рецептами</h1>
      <nav>
        <ul>
          <li>
            <Link to="/categories">Категории</Link>
          </li>
          <li>
            <Link to="/recipes">Все рецепты</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;
