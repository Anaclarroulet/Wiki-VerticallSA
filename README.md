# Wiki-VerticallSA
Wiki Verticall SA – Proyecto de Práctica Profesional

Este repositorio contiene el desarrollo técnico de una propuesta de mejora para la empresa Verticall SA, orientada a la implementación de una herramienta de gestión del conocimiento basada en Wiki.js y tecnologías de IA generativa.

Objetivo

Diseñar e implementar una wiki interna, modular, mantenible y sincronizada con GitHub, que documente el uso operativo del sistema Verticall BPM/CRM, y que a futuro pueda ser base de un asistente inteligente con IA.

Estructura del repositorio

Wiki-VerticallSA/
├── doc/
│ ├── infra/ # Configuración técnica (Docker)
│ ├── manuales/ # Guías de uso
│ └── diagramas/ # Mapas y esquemas (opcional)
├── prototipo-ia/ # Prototipo de asistente inteligente
│ ├── app.py
│ └── docs/ # Contenido indexado
├── procesos-del-sistema/ # Artículos organizados por procesos
└── README.md

Tecnologías utilizadas

- [Wiki.js](https://js.wiki/)
- [Docker](https://www.docker.com/)
- [Railway](https://railway.app/)
- [LangChain](https://www.langchain.com/)
- [Gradio](https://www.gradio.app/)
- [OpenAI API](https://platform.openai.com/)
- [GitHub](https://github.com/)

Documentos importantes

- [`docker-compose.yml`](doc/infra/docker-compose.yml) – configuración del entorno
- [`Manual_Basico_Wiki_Verticall.docx`](doc/manuales/) – guía de uso
- [`wiki-iag-prototipo`](prototipo-ia/) – integración IA + contenido
