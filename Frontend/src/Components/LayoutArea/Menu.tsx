/** Main navigation menu for switching between Home and About pages. */
import { useMemo } from "react";
import { NavLink } from "react-router-dom";
import "./Menu.css";

const GLYPHS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const GLYPH_COUNT = 20;
const COLUMN_COUNT = 14;

function randomGlyphs(count: number): string[] {
  return Array.from({ length: count }, () => GLYPHS[Math.floor(Math.random() * GLYPHS.length)]);
}

export function Menu() {
  const columns = useMemo(
    () =>
      Array.from({ length: COLUMN_COUNT }, (_, index) => ({
        id: index,
        glyphs: randomGlyphs(GLYPH_COUNT),
        duration: 4 + Math.random() * 7,
        delay: Math.random() * -12,
      })),
    [],
  );

  return (
    <nav className="menu">
      <div className="menu-rain" aria-hidden="true">
        {columns.map((column) => (
          <div key={column.id} className="menu-rain-column">
            <div
              className="menu-rain-track"
              style={{
                animationDuration: `${column.duration}s`,
                animationDelay: `${column.delay}s`,
              }}
            >
              {[...column.glyphs, ...column.glyphs].map((glyph, glyphIndex) => (
                <span
                  key={glyphIndex}
                  className={`menu-rain-glyph menu-rain-glyph--${glyphIndex % 3}`}
                >
                  {glyph}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="menu-links">
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
      </div>
    </nav>
  );
}
