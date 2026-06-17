/** Main navigation menu for switching between Home and About pages. */
import { NavLink } from "react-router-dom";
import "./Menu.css";

export function Menu() {
  return (
    <nav className="menu">
      <NavLink to="/">Home</NavLink>
      <NavLink to="/about">About</NavLink>
    </nav>
  );
}
