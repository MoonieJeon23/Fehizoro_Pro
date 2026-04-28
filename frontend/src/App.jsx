import React, { useState, useEffect } from 'react';
import photoProfil from './assets/fehizoro-hero.jpg';
import lotusBg from './assets/lotus.png';

const API_BASE_URL = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
  ? "http://127.0.0.1:8000/api"
  : "https://mooniejeon23.pythonanywhere.com/api";

function App() {
  const [projects, setProjects] = useState([]);
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    Promise.all([
      fetch(API_BASE_URL + "projects/").then(res => res.json()),
      fetch(API_BASE_URL + "skills/").then(res => res.json())
    ])
    .then(([projectsData, skillsData]) => {
      setProjects(Array.isArray(projectsData) ? projectsData : []);
      setSkills(Array.isArray(skillsData) ? skillsData : []);
    })
    .catch(err => console.error("Erreur de synchronisation :", err));
  }, []);

  const handleCopyEmail = () => {
    navigator.clipboard.writeText('rakotoarisonfehizoro23@gmail.com');
    alert("Email copié dans le presse-papiers ! ✨");
  };

  return (
    <div className="relative w-full min-h-screen bg-[#050205] overflow-x-hidden font-sans"
         style={{ backgroundImage: 'radial-gradient(circle at 20% 30%, #1a0b1a 0%, #050205 70%)' }}>

      {/* BACKGROUND : LOTUS GÉANT */}
      <div className="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img
          src={lotusBg}
          className="absolute max-none opacity-45 animate-float"
          style={{
            width: '1200px',
            height: 'auto',
            minWidth: '1200px',
            top: '-50px',
            left: '50%',
            marginLeft: '-600px',
            display: 'block',
            filter: 'drop-shadow(0 0 20px rgba(228, 177, 171, 0.2))'
          }}
          alt="Lotus Background"
        />
        <div className="absolute w-[1000px] h-[1000px] bg-purple-900/30 blur-[120px] rounded-full top-0 left-1/2 -ml-[500px] -z-10"></div>
      </div>

      <main className="relative z-10 container mx-auto px-6 lg:px-12 py-12 flex flex-col">

        <nav className="flex justify-between items-center py-4 border-b border-rose-gold/10 backdrop-blur-md">
          <span className="text-sm tracking-[0.3em] font-light text-rose-gold/80 uppercase">Fehizoro Ingenierie</span>
          <div className="hidden md:flex space-x-8 text-xs tracking-widest text-gray-400">
            <a href="#projects" className="hover:text-rose-gold transition uppercase">Projects</a>
            <a href="#skills" className="hover:text-rose-gold transition uppercase">Skills</a>
            <a href="#contact" className="hover:text-rose-gold transition uppercase">Contact</a>
          </div>
        </nav>

        {/* SECTION HERO */}
        <div className="flex flex-col lg:flex-row justify-between items-center py-20 gap-4">
          <div className="lg:w-[70%] space-y-6 z-50">
            <h2 className="text-rose-gold/60 text-lg font-bold tracking-widest uppercase">
              Software Developer & Designer
            </h2>
            <div className="w-full overflow-visible">
              <h1 className="text-[clamp(3rem,12vw,9rem)] font-black leading-none text-mirror-rosegold whitespace-nowrap uppercase tracking-tighter">
                FEHIZORO
              </h1>
            </div>
            <p className="text-gray-400 max-w-md leading-relaxed text-lg">
              Créer des solutions robustes et des expériences visuelles immersives.
              Mon expertise fusionne la rigueur du code et l'esthétique de la 3D.
            </p>
            <a
              href="../media/CV_Fehizoro.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="px-10 py-3 rounded-md border border-rose-gold text-rose-gold text-sm font-bold hover:bg-rose-gold hover:text-black transition-all duration-500 uppercase tracking-widest inline-block"
            >
              MON CV
            </a>
          </div>

          <div className="relative lg:w-[30%] flex justify-end">
            <div className="w-64 h-64 lg:w-80 lg:h-80 rounded-full border-2 border-rose-gold/30 p-3 bg-black/20 backdrop-blur-sm">
              <div className="w-full h-full rounded-full border-[6px] border-rose-gold overflow-hidden neon-border">
                <img src={photoProfil} className="w-full h-full object-cover scale-110" alt="Portrait" />
              </div>
            </div>
            <div className="absolute bottom-1 right-1 w-26 h-26 bg-black border-2 border-rose-gold rounded-full flex items-center justify-center neon-border shadow-[0_0_25px_rgba(228,177,171,0.4)] overflow-hidden">
              <img src={lotusBg} className="w-26 opacity-100 scale-110" alt="" />
            </div>
          </div>
        </div>

        {/* PROJETS RÉCENTS */}
        <div id="projects" className="space-y-12 pb-20">
          <h3 className="text-sm tracking-[0.5em] text-gray-500 uppercase">Projets Récents</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project) => (
              <div key={project.id} className="group relative flex flex-col bg-[#120a12]/60 border border-rose-gold/20 rounded-xl backdrop-blur-md p-6 hover:border-rose-gold/50 transition-all duration-500 h-full shadow-lg">
                <div className="relative z-10 flex flex-col h-full">
                  <div className="w-full aspect-video bg-black/40 rounded-lg mb-4 overflow-hidden">
                    {project.image ? (
                      <img src={project.image} alt={project.title} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                    ) : (
                      <div className="w-full h-full bg-black/20" />
                    )}
                  </div>
                  <div className="flex-grow">
                    <h4 className="text-rose-gold font-bold text-2xl uppercase tracking-wider leading-tight">{project.title}</h4>
                    <p className="text-gray-400 text-sm mt-4 leading-relaxed">{project.description}</p>
                  </div>
                  <div className="flex gap-2 flex-wrap mt-8">
                    {project.technology_stack?.split(',').map((tech, index) => (
                      <span key={index} className="text-xs text-rose-gold/80 border border-rose-gold/20 px-3 py-1.5 rounded bg-rose-gold/5 font-medium">
                        {tech.trim()}
                      </span>
                    ))}
                  </div>
                </div>
                <img src={lotusBg} className="absolute -bottom-4 -right-4 w-45 opacity-15 group-hover:opacity-40 group-hover:rotate-12 transition-all duration-1000 mix-blend-screen pointer-events-none" alt="" />
                {project.github_link && <a href={project.github_link} target="_blank" rel="noopener noreferrer" className="absolute inset-0 z-20" />}
              </div>
            ))}
          </div>
        </div>

        {/* SECTION SKILLS */}
        <section id="skills" className="py-32 relative">
          <h3 className="text-sm tracking-[0.5em] text-gray-500 uppercase mb-24 text-center">Expertises & Skills</h3>
          <div className="flex flex-col lg:flex-row justify-center gap-16 items-center px-4">
            <div className="flex-1 w-full max-w-sm space-y-8 lg:text-right">
              <h4 className="text-rose-gold font-bold tracking-[0.3em] text-md uppercase lg:border-r-2 border-l-2 lg:border-l-0 border-rose-gold lg:pr-6 pl-6 lg:pl-0">
                Development & Tools
              </h4>
              <div className="flex flex-wrap lg:justify-end gap-4">
                {skills.filter(s => s.category === 'DEV').map(skill => (
                  <div key={skill.id} className="px-5 py-2.5 bg-[#120a12]/80 border border-rose-gold/20 rounded-full backdrop-blur-md text-gray-200 text-xs md:text-sm hover:border-rose-gold hover:text-rose-gold transition-all cursor-default font-medium tracking-wide shadow-lg">
                    {skill.name}
                  </div>
                ))}
              </div>
            </div>

            <div className="relative w-70 h-70 flex items-center justify-center">
               <img src={lotusBg} className="w-full opacity-80 animate-pulse drop-shadow-[0_0_30px_rgba(228,177,171,0.5)]" alt="Lotus Central" />
               <div className="absolute inset-0 bg-rose-gold/10 blur-[120px] rounded-full -z-10"></div>
            </div>

            <div className="flex-1 w-full max-w-sm space-y-8">
              <h4 className="text-rose-gold font-bold tracking-[0.3em] text-md uppercase border-l-2 border-rose-gold pl-6">
                  Tools & Soft Skills
              </h4>
              <div className="flex flex-wrap gap-4">
                {skills.filter(s => s.category !== 'DEV').map(skill => (
                  <div key={skill.id} className="px-5 py-2.5 bg-[#120a12]/80 border border-rose-gold/20 rounded-full backdrop-blur-md text-gray-200 text-xs md:text-sm hover:border-rose-gold hover:text-rose-gold transition-all cursor-default font-medium tracking-wide shadow-lg">
                    {skill.name}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* SECTION CONTACT SIMPLIFIÉE */}
        <section id="contact" className="py-20 relative">
          <div className="max-w-3xl mx-auto px-4">
            <h3 className="text-sm tracking-[0.5em] text-gray-500 uppercase mb-12 text-center">
              Me contacter
            </h3>

            <div className="bg-[#120a12]/60 border border-rose-gold/20 rounded-2xl backdrop-blur-md p-10 shadow-2xl relative overflow-hidden text-center">
              <img src={lotusBg} className="absolute -bottom-10 -right-10 w-64 opacity-5 pointer-events-none" alt="" />

              <p className="text-gray-400 text-sm mb-8 tracking-widest leading-relaxed uppercase">
                Pour toute collaboration ou demande de projet, <br/> mon email est à votre disposition.
              </p>

              {/* BOÎTE EMAIL */}
              <div className="flex flex-col md:flex-row items-center justify-between gap-6 p-6 bg-black/40 border border-rose-gold/30 rounded-xl mb-12">
                <span className="text-xl md:text-2xl text-rose-gold font-light tracking-wider break-all">
                  kookiesunshine23@gmail.com
                </span>
                <button
                  onClick={handleCopyEmail}
                  className="px-8 py-3 bg-rose-gold/10 border border-rose-gold text-rose-gold text-xs font-bold hover:bg-rose-gold hover:text-black transition-all duration-300 uppercase tracking-[0.2em] whitespace-nowrap rounded"
                >
                  Copier le mail
                </button>
              </div>

              {/* RÉSEAUX SOCIAUX DANS LE CONTENEUR */}
              <div className="flex flex-wrap justify-center gap-8 md:gap-12">
                <a href="https://github.com/MoonieJeon23" target="_blank" rel="noreferrer" className="text-xs tracking-[0.3em] text-gray-500 hover:text-rose-gold transition uppercase font-bold">Github</a>
                <a href="https://www.linkedin.com/in/fehizoro-rakotoarison" target="_blank" rel="noreferrer" className="text-xs tracking-[0.3em] text-gray-500 hover:text-rose-gold transition uppercase font-bold">Linkedin</a>
                <a href="https://www.instagram.com/fehizoro_23" target="_blank" rel="noreferrer" className="text-xs tracking-[0.3em] text-gray-500 hover:text-rose-gold transition uppercase font-bold">Instagram</a>
                <a href="https://wa.me/261335845808" target="_blank" rel="noreferrer" className="text-xs tracking-[0.3em] text-gray-500 hover:text-rose-gold transition uppercase font-bold">Whatsapp</a>
              </div>
            </div>
          </div>
        </section>

        {/* FOOTER */}
        <footer className="mt-24 py-12 border-t border-rose-gold/10 text-center space-y-4">
          <p className="text-[10px] text-gray-600 tracking-[0.5em] uppercase">© 2026 FEHIZORO RAKOTOARISON — Antananarivo, Madagascar</p>
          <p className="text-[9px] text-gray-700 tracking-[0.2em] uppercase">Built with Django & React</p>
        </footer>

      </main>
    </div>
  );
}

export default App;