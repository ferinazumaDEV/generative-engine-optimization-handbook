<!-- synced-from: bb01ec297d9e90fcafb1de784064929b7c0d0c56 -->

# The GEO Handbook

**Español** · [English](README.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22299644.svg)](https://doi.org/10.5281/zenodo.22299644)

**Todo sobre la optimización para motores generativos, en un solo sitio.** Desde *«¿qué es GEO y por dónde empiezo?»* hasta la lista técnica, el método de medición y la investigación primaria — lo que necesites para que tu contenido lo entiendan y lo **citen los motores de respuesta de IA** (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot) está aquí. De principiante a profesional, y **cada afirmación lleva una fuente real y verificable, o una marca explícita de que está pendiente de verificar**.

> La **optimización para motores generativos** (*generative engine optimization*, GEO) es la práctica de estructurar, escribir y publicar contenido para que los motores generativos de IA —ChatGPT, Perplexity, Google AI Overviews / AI Mode, Gemini y Copilot— lo entiendan, se fíen de él y **lo citen** al responder a alguien.

El término se acuñó en el artículo revisado por pares *«GEO: Generative Engine Optimization»* (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan y Deshpande), presentado en **KDD 2024** — [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900). Aquel estudio fue el primero en demostrar, en un experimento controlado, que el contenido se puede optimizar deliberadamente para ganar visibilidad en las respuestas generadas por IA, con mejoras de visibilidad de **hasta el 40%** a partir de señales de contenido como citar fuentes, añadir estadísticas o recoger a autoridades solventes (el mejor método sobre la mejor métrica, medido en un motor de la época de GPT-3.5 en 2023-24 — un techo, no una media; ver [07 · Investigación](docs/07-research-cases.md)).

> **Nota sobre el idioma.** Este README está en las dos lenguas; **los nueve capítulos están sólo en inglés**, y es deliberado: traducir 55.000 palabras que cambian cada semana crearía dos versiones que acabarían diciendo cosas distintas, y una traducción desactualizada es peor que ninguna. Si eso cambia, lo dirá esta nota.

## Ficha de identidad GEO

La versión legible por máquina de esta tabla es [`about.jsonld`](about.jsonld) (JSON-LD de schema.org). Ese fichero es la fuente de verdad; esta tabla lo refleja campo a campo.

| Campo | Valor |
|---|---|
| Tipo | `CreativeWork` — *The GEO Handbook* |
| Autor | Fernando Aporta Franco (ferinazumaDEV) · sameAs: [github.com/ferinazumaDEV](https://github.com/ferinazumaDEV), [zentimes.es](https://zentimes.es) |
| Resumen | Referencia completa y con fuentes sobre optimización para motores generativos (GEO): estructurar, escribir y publicar contenido para que los motores de respuesta de IA lo entiendan, se fíen de él y lo citen. |
| Basado en | [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) — Aggarwal et al., *GEO: Generative Engine Optimization*, KDD 2024 |
| Fuentes | Cita a nivel de obra: [arXiv:2311.09735](https://arxiv.org/abs/2311.09735). Cada capítulo lista las suyas, primero las primarias; las secundarias (de industria) van etiquetadas como tales |
| Cómo citarlo | DOI [10.5281/zenodo.22299644](https://doi.org/10.5281/zenodo.22299644) (DOI de concepto, siempre la última versión) — [`CITATION.cff`](CITATION.cff) |
| URL canónica | <https://github.com/ferinazumaDEV/generative-engine-optimization-handbook> |
| Licencia | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| Versión | 0.1.2 |
| Publicado | 2026-08-25 |
| Última modificación | 2026-09-06 |
| Madurez | `mixed` · reproducible: `no` — ver [CLAIMS.md](CLAIMS.md) |

---

## Por qué existe

La búsqueda está pasando de una lista de enlaces azules a **una sola respuesta sintetizada**. Cuando alguien le pregunta algo a ChatGPT o a Perplexity, el modelo redacta una respuesta y —cada vez más— cita un puñado de fuentes. Si tu contenido no está en ese puñado, eres invisible, por muy bien que rankeara en el Google de siempre.

El SEO clásico optimiza para **rankear una página**. El **GEO optimiza para que te citen dentro de la respuesta.** Se solapan, pero no son lo mismo, y las tácticas que mueven la aguja son distintas (y todavía se están descubriendo).

Este manual es una **referencia libre, pública y mantenida por la comunidad** sobre cómo los motores generativos seleccionan, citan y sintetizan fuentes, y qué puede hacer al respecto quien publica. Está escrito para que le sirva a alguien que **empieza** («¿qué es esto y por dónde tiro?») y a alguien que **ya trabaja en esto** («dame la lista técnica y el método de medición»). Aspira a ser *exacto y actual*, a **citar fuentes reales y verificables**, y a crecer cada semana con aportaciones de fuera.

**Palabras clave:** optimización para motores generativos, GEO, generative engine optimization, optimización para búsqueda con IA, SEO para IA, LLM SEO, AEO (optimización para motores de respuesta), cómo conseguir que te cite ChatGPT / Perplexity / Google AI Overviews, visibilidad en RAG, citas de LLM.

---

## Índice

Los capítulos están en inglés.

| # | Capítulo | Qué cubre |
|---|---------|----------------|
| 01 | [Foundations](docs/01-foundations.md) | Qué es GEO, GEO frente a SEO y AEO, cómo recuperan y citan los motores generativos, vocabulario básico |
| 02 | [The Engines](docs/02-engines.md) | ChatGPT Search, Perplexity, Google AI Overviews / AI Mode, Gemini, Copilot — cómo recupera y cita cada uno, y en qué se diferencian |
| 03 | [Content Strategy](docs/03-content.md) | Escribir contenido extraíble y citable: estructura, datos citables, formato apto para trocear, claridad de entidad |
| 04 | [Technical GEO](docs/04-technical.md) | Rastreabilidad para bots de IA, `robots.txt` y user-agents de IA, datos estructurados, `llms.txt`, feeds, renderizado |
| 05 | [Authority & Trust](docs/05-authority.md) | E-E-A-T para máquinas, entidades y grafos de conocimiento, citas, menciones de marca, presencia fuera del sitio |
| 06 | [Measurement](docs/06-measurement.md) | Cómo medir visibilidad y cuota de citación en IA, herramientas, tráfico de referencia desde IA, KPIs |
| 07 | [Research & Case Studies](docs/07-research-cases.md) | La literatura primaria, experimentos reproducibles y casos documentados (con cita) |
| 08 | [Future & Ethics](docs/08-future-ethics.md) | Hacia dónde va el GEO, riesgos de manipulación de prompts y respuestas, transparencia, y hacerlo con responsabilidad |
| 09 | [Glossary](docs/09-glossary.md) | Definiciones en lenguaje llano de cada término del manual |

> Los nueve capítulos están escritos y con fuentes (más de 100 citadas a lo largo del texto — primarias donde las hay, las secundarias etiquetadas). Son documentos vivos que se actualizan cada semana — [se agradecen aportaciones y correcciones](CONTRIBUTING.md).

---

## Cómo contribuir

Este manual sólo sigue siendo exacto si la gente lo mantiene exacto. En **[CONTRIBUTING.md](CONTRIBUTING.md)** está el proceso de PR y la guía de estilo. La única regla innegociable: **cada afirmación lleva una fuente real y enlazable, o va marcada explícitamente como `needs verification`.** Ni hechos inventados ni citas fabricadas.

- ¿Has visto algo desactualizado o mal? Abre una incidencia.
- ¿Tienes una técnica nueva *con fuente*? Usa la [plantilla de nueva técnica](.github/ISSUE_TEMPLATE/new-technique.md) o abre un PR.
- Las correcciones pequeñas (erratas, enlaces muertos) siempre son bienvenidas.

Puedes escribir en español o en inglés.

## Cadencia semanal

El GEO cambia rápido: los motores publican, citan distinto y exponen controles nuevos casi cada semana. Para no quedarse atrás:

- Cada semana se publica un registro fechado en **[`updates/`](updates/README.md)** (por ejemplo `updates/2026-W35.md`) que resume *qué cambió en el panorama GEO* y *qué cambió en este repositorio*.
- Un resumen de los cambios relevantes vive en **[CHANGELOG.md](CHANGELOG.md)** (formato Keep a Changelog).
- Cadencia objetivo: **una entrada por semana ISO.** Las semanas sin nada relevante llevan igualmente una nota corta de «sin cambios materiales», para que el registro sea continuo.

## Cómo citarlo

Cada versión etiquetada se archiva en Zenodo con DOI. Cita el **DOI de concepto**: resuelve siempre a la última versión. Cada versión tiene además su propio DOI en su ficha, por si necesitas fijar un estado exacto del texto.

> Aporta Franco, Fernando. *The GEO Handbook*. Zenodo, 2026. <https://doi.org/10.5281/zenodo.22299644>.

Los mismos metadatos están en [`CITATION.cff`](CITATION.cff) — el botón **«Cite this repository»** de GitHub los presenta en APA o BibTeX.

## Licencia

El contenido está bajo **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](LICENSE)**. Puedes compartir y adaptar el material, incluso comercialmente, siempre que des el crédito adecuado y licencies lo que derives bajo los mismos términos. Texto completo: <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

## Autor y mantenedor

Creado y mantenido por Fernando Aporta Franco (ferinazumaDEV). Las aportaciones se acreditan a quien las hace; están en el changelog y en el historial de PRs. Si construyes sobre esto, se agradece la atribución a *«The GEO Handbook — Fernando Aporta Franco, CC BY-SA 4.0»*.

## Parte de un conjunto de trabajo abierto

<!-- ecosystem:start -->
Parte de un conjunto de trabajo abierto sobre hacer el contenido legible para las máquinas, de **Fernando Aporta Franco** ([ferinazumaDEV](https://github.com/ferinazumaDEV)):

**Tres capas sobre GEO (optimización para motores generativos)**
- **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)** — la referencia: qué hacer y por qué, con fuentes (teoría).
- **[The GEO Cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook)** — seis recetas antes/después reproducibles con mediciones offline (práctica).
- **[Evidence-Based Prompt Engineering](https://github.com/ferinazumaDEV/prompt-engineering-evidence)** — un registro clasificado y con fuentes de técnicas de prompting (el lado de la entrada).

**Herramientas abiertas pequeñas**
- [typedout](https://github.com/ferinazumaDEV/typedout) — salida estructurada fiable de OpenAI y Anthropic, con interfaz de proveedor para añadir otros.
- [politeclient](https://github.com/ferinazumaDEV/politeclient) — cliente HTTP educado para Python: reintentos con espera, límite de ritmo por host, caché, paginación.
- [webhook-replay](https://github.com/ferinazumaDEV/webhook-replay) — captura un webhook una vez y reprodúcelo contra tu aplicación local las veces que haga falta.
- [scaffld](https://github.com/ferinazumaDEV/scaffld) — genera proyectos Python completos desde plantillas, con interfaz de terminal.
- [framesig](https://github.com/ferinazumaDEV/framesig) — encuentra eventos en pantalla dentro de un vídeo por su firma de píxeles; sin aprendizaje automático.
- [notebooklm-kb-system](https://github.com/ferinazumaDEV/notebooklm-kb-system) — un segundo cerebro eficiente en tokens para agentes de IA sobre NotebookLM.

Web y publicaciones: **[zentimes.es](https://zentimes.es)**.
<!-- ecosystem:end -->

Más en **[github.com/ferinazumaDEV](https://github.com/ferinazumaDEV)**.

---

*Este es un proyecto sólo de documentación. No contiene código, ni seguimiento, ni datos privados. Todo lo que hay aquí es público y está pensado para reutilizarse.*
