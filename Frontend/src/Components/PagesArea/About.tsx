/** About page with project and developer information. */
import AnnaPortrait from "../../assets/images/Anna.Lempert.jpeg";
import "./About.css";

export function About() {
  return (
    <section className="about">
      <div className="about-media">
        <img src={AnnaPortrait} alt="Anna Lempert" className="about-photo" />
      </div>
      <div className="about-content">
        <span className="about-badge">Project Profile</span>
        <h2>About This Project</h2>
        <p>
          This project is a ChatGPT-like web application built with a FastAPI backend, a React TypeScript frontend,
          and a MySQL database. The frontend talks only to the backend, and the backend handles OpenAI API requests.
          This project uses the "Clean Architecture" and the "Reusable Service Modules" pattern.
        </p>
        <h3>Developer</h3>
        <p>
          Anna Lempert - Full Stack Developer & Oracle Applicative DBA.
          <br />
          Expirienced in React, TypeScript, Node.js, FastAPI, MySQL, MongoDB, Docker, and Python.
          <br />
          Graduated from John Bryce college.
          <br />
          27 years experience in the field of software development - PL-SQL, Oracle, Cobol, C.
        </p>
        <div className="about-links">
          <a
            className="about-link about-link-linkedin"
            href="https://www.linkedin.com/in/anna-lempert-a6355350/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span className="about-link-icon" aria-hidden="true">in</span>
            <span className="about-link-text">
              <span className="about-link-label">Connect on</span>
              <span className="about-link-name">LinkedIn</span>
            </span>
            <span className="about-link-arrow" aria-hidden="true">→</span>
          </a>
          <a
            className="about-link about-link-github"
            href="https://github.com/AnnaLempert"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span className="about-link-icon" aria-hidden="true">gh</span>
            <span className="about-link-text">
              <span className="about-link-label">View profile on</span>
              <span className="about-link-name">GitHub</span>
            </span>
            <span className="about-link-arrow" aria-hidden="true">→</span>
          </a>
        </div>
      </div>
    </section>
  );
}
