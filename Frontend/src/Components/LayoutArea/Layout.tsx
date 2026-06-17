/**
 * Main application layout with header, navigation menu, and routed page content.
 */
import { Route, Routes } from "react-router-dom";
import { Header } from "./Header";
import { Menu } from "./Menu";
import { Home } from "../PagesArea/Home";
import { About } from "../PagesArea/About";
import { Page404 } from "../PagesArea/Page404";
import "./Layout.css";

export function Layout() {
  return (
    <div className="layout">
      <Header />
      <Menu />
      <main className="layout-main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<Page404 />} />
        </Routes>
      </main>
    </div>
  );
}
