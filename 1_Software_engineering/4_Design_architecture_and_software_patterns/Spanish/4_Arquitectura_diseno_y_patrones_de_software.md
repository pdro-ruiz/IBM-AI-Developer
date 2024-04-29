# Arquitectura, diseno y patrones de software

## Arquitecura y diseno de software

### Introducción a la Arquitectura de Software

#### **Concepto de Arquitectura de Software**
   - **Definición**:
     - La arquitectura de software es la organización estructurada de un sistema de software que describe sus componentes principales, sus relaciones y cómo interactúan para cumplir con los requisitos funcionales y no funcionales del sistema.
   - **Propósito**:
     - Actúa como un plano para el sistema, proporcionando un marco que guía tanto el desarrollo técnico como la toma de decisiones estratégicas.

#### **Importancia de una Arquitectura de Software Bien Diseñada**
   - **Balance de Necesidades**:
     - Una arquitectura bien diseñada equilibra las necesidades de diversas partes interesadas, incluyendo desarrolladores, gerentes de proyecto y usuarios finales.
   - **Facilitación de la Comunicación**:
     - Sirve como un documento vital para la comunicación entre los miembros del equipo de desarrollo y otras partes interesadas, asegurando que todos entiendan la estructura y el diseño del sistema.
   - **Adaptabilidad**:
     - Permite al sistema adaptarse a cambios en los requisitos y tecnologías a lo largo de su ciclo de vida, manteniendo la integridad del sistema y evitando la obsolescencia.

#### **Influencia en Decisiones de Diseño y Tecnológicas**
   - **Elección de Pilas Tecnológicas**:
     - La arquitectura de software guía la selección de las pilas tecnológicas apropiadas, asegurando que las tecnologías elegidas soporten adecuadamente los requisitos del sistema, incluyendo la seguridad, el rendimiento y la escalabilidad.
   - **Entornos de Producción**:
     - Determina las necesidades del entorno de producción, incluyendo la infraestructura necesaria como servidores, bases de datos y equilibradores de carga, para asegurar un despliegue y operación eficientes del sistema.

#### **Artefactos de Diseño de la Arquitectura de Software**
   - **Documento de Diseño de Software (SDD)**:
     - Un documento técnico que detalla el diseño del sistema, incluyendo especificaciones, supuestos, dependencias, y restricciones.
   - **Diagrama Arquitectónico**:
     - Representa visualmente los componentes del sistema, sus interacciones y las restricciones arquitectónicas.
   - **Diagramas UML**:
     - Utilizados para modelar visualmente la estructura y el comportamiento del sistema mediante una notación estándar que es agnóstica al lenguaje de programación.

#### **Patrones Arquitectónicos**
   - **Uso de Patrones Arquitectónicos**:
     - Los patrones arquitectónicos son soluciones probadas a problemas comunes en la arquitectura de software. Proporcionan un enfoque estandarizado para resolver problemas de diseño y pueden ser reutilizados en diferentes proyectos.

#### **Beneficios de un Buen Diseño Arquitectónico**
   - **Cohesión y Consistencia**:
     - Fomenta un desarrollo coherente y consistente al proporcionar una guía clara sobre cómo deben construirse e interactuar los componentes del sistema.
   - **Mantenibilidad y Escalabilidad**:
     - Facilita la mantenibilidad y la escalabilidad al asegurar que la arquitectura soporte tanto las necesidades actuales como las futuras expansiones o modificaciones.


### Diseño y Modelado de Software

#### **Diseño Estructurado vs. Modelos de Comportamiento**
   - **Diseño Estructurado**:
     - Conceptualiza un problema de software en elementos de solución más pequeños y bien organizados llamados módulos y submódulos.
     - Enfatiza la cohesión dentro de los módulos y un acoplamiento débil entre ellos, lo que facilita la mantenibilidad y escalabilidad del software.
   - **Modelos de Comportamiento**:
     - Describen lo que hace un sistema sin especificar cómo se implementa ese comportamiento.
     - Utilizan diagramas como el diagrama de transición de estado y diagramas de interacción para representar el flujo de acciones y eventos dentro del sistema.

#### **Lenguaje de Modelado Unificado (UML)**
   - **Propósito y Ventajas**:
     - UML es un lenguaje de modelado estandarizado utilizado para visualizar, especificar, construir y documentar los artefactos de un sistema de software.
     - Ayuda a planificar funciones antes de la codificación, facilita la incorporación de nuevos miembros al equipo, y mejora la comunicación entre los técnicos y los no técnicos.
   - **Tipos de Diagramas UML**:
     - **Estructurales**: Incluyen diagramas de clases, objetos, y componentes que describen la estructura física del sistema.
     - **De comportamiento**: Incluyen diagramas de casos de uso, actividades, secuencias, y estados que describen la dinámica y el flujo del sistema.

#### **Interacción y Diagrama de Transición de Estado**
   - **Diagrama de Transición de Estado**:
     - Modela los diferentes estados de un sistema y los eventos que causan transiciones entre esos estados.
     - Por ejemplo, en un sistema de atención médica, puede modelar estados como "esperar", "hacerse pruebas", y "con el médico".
   - **Diagrama de Interacción**:
     - Se utiliza para mostrar la interacción y la comunicación entre objetos a lo largo del tiempo en un sistema de software.
     - Un ejemplo es un diagrama de secuencia que muestra cómo un paciente agenda una cita en un portal en línea.

#### **Importancia del Modelado en el Diseño de Software**
   - **Facilita la Comprensión**:
     - Los diagramas y modelos ayudan a los desarrolladores y partes interesadas a entender el sistema y sus interacciones de manera más clara y concisa.
   - **Soporte para Desarrollo Ágil**:
     - Permite iteraciones rápidas y adaptativas del diseño y la arquitectura del software en respuesta a los requisitos cambiantes y mejoras propuestas.

#### **Integración de Diseño Estructurado y Modelos de Comportamiento**
   - **Sinergia entre Diseño y Comportamiento**:
     - Integrar ambos enfoques proporciona una visión completa del sistema, combinando una estructura sólida con una comprensión detallada de las operaciones y flujos del sistema.
   - **Aplicaciones Prácticas**:
     - En el diseño de aplicaciones empresariales, sistemas embebidos, o cualquier software complejo, la combinación de estos métodos mejora significativamente la eficiencia del desarrollo y la calidad del producto final.



### Análisis y Diseño Orientados a Objetos (OOAD)

#### **Conceptos Fundamentales de OOAD**
   - **Objetos**:
     - Son entidades que encapsulan datos y comportamientos (métodos) asociados. Los objetos son instancias de clases y pueden representar entidades del mundo real o conceptos abstractos dentro de un sistema.
   - **Clases**:
     - Actúan como plantillas o planos para crear objetos. Definen atributos (datos) y métodos (funciones o comportamientos) que sus instancias (objetos) tendrán.

#### **Propósito de un Diagrama de Clases**
   - **Definición**:
     - Un diagrama de clases es una representación visual que muestra la estructura de las clases dentro de un sistema, sus atributos, métodos y las relaciones entre ellas, como herencia y asociaciones.
   - **Utilidad**:
     - Facilita la comprensión de cómo está organizado un sistema y cómo interactúan sus componentes. Es esencial para la documentación y la planificación en el desarrollo de software orientado a objetos.

#### **Diseño Orientado a Objetos y su Relación con la Arquitectura de Software**
   - **Integración en la Arquitectura**:
     - El diseño orientado a objetos se integra profundamente en la arquitectura de software, proporcionando un marco para descomponer un sistema en componentes manejables con interacciones claramente definidas.
   - **Beneficios**:
     - Promueve la reutilización de código a través de la herencia y el polimorfismo, facilita la escalabilidad y la mantenibilidad del sistema, y soporta la modularidad en el diseño de software.

#### **Explicación de los Diagramas UML**
   - **Diagramas de Clases**:
     - Detallan las clases, sus campos, métodos y relaciones en un formato estandarizado que es independiente del lenguaje de programación.
   - **Diagramas de Comportamiento**:
     - Incluyen diagramas de casos de uso, actividades, secuencias y estados que muestran cómo los usuarios interactúan con el sistema y cómo el sistema responde a esas interacciones.

#### **Importancia de OOAD en el Desarrollo de Software**
   - **Análisis y Diseño**:
     - OOAD ayuda a identificar requisitos de software y a diseñar soluciones que alinean la funcionalidad del software con las necesidades del negocio o del usuario.
   - **Implementación**:
     - Facilita la implementación de sistemas complejos al dividir el problema en partes más pequeñas y manejables que son más fáciles de entender, desarrollar y probar.

#### **Implicaciones Prácticas de OOAD**
   - **Trabajo Colaborativo**:
     - Permite que múltiples desarrolladores trabajen en diferentes partes del sistema simultáneamente, mejorando la eficiencia y reduciendo el tiempo de desarrollo.
   - **Mantenibilidad**:
     - Los sistemas diseñados usando OOAD son más fáciles de mantener y actualizar debido a su estructura modular y al uso de principios de encapsulación y abstracción.



## Patrones de arquitectura de software 


### Enfoques de la Arquitectura de Aplicaciones

#### **Componentes y Servicios en Arquitecturas de Software**
   - **Características de un Componente**:
     - **Reutilizable**: Diseñados para ser utilizados en varios sistemas o aplicaciones diferentes.
     - **Reemplazable**: Pueden ser intercambiados fácilmente por otros componentes similares.
     - **Independiente**: Funcionan sin depender críticamente de otros componentes.
     - **Extensible**: Permiten añadir nuevas funcionalidades sin modificar el componente en sí.
     - **Encapsulado**: Encierran datos y comportamientos, ocultando los detalles internos.
     - **No específicos del contexto**: Funcionan en diferentes entornos sin necesidad de modificar su código.

   - **Componentes vs. Servicios**:
     - Los componentes son unidades de funcionalidad dentro de una aplicación, mientras que los servicios son componentes diseñados para ser utilizados de manera independiente y a menudo en múltiples sistemas, siguiendo el enfoque de una Arquitectura Orientada a Servicios (SOA).

#### **Arquitectura Basada en Componentes**
   - **Definición**:
     - Una arquitectura que estructura una aplicación como un conjunto de componentes intercambiables y modulares.
   - **Beneficios**:
     - Facilita la mantenibilidad y la escalabilidad del software al permitir cambios y mejoras sin afectar otros componentes del sistema.

#### **Arquitectura Orientada a Servicios (SOA)**
   - **Características**:
     - Los servicios en SOA son autónomos y encapsulan una funcionalidad de negocio completa, ofreciendo interoperabilidad entre diferentes sistemas y tecnologías.
   - **Ventajas**:
     - Promueve la reutilización de servicios, lo que reduce el costo y el tiempo de desarrollo.
     - Permite una integración flexible y dinámica de servicios de software empresarial.

#### **Sistemas Distribuidos**
   - **Definición**:
     - Consiste en componentes ubicados en diferentes sistemas de red que comunican y coordinan sus acciones solo mediante el paso de mensajes.
   - **Características**:
     - **Tolerancia a fallos**: Pueden continuar funcionando correctamente incluso si parte del sistema falla.
     - **Concurrencia**: Realizan varias operaciones al mismo tiempo, mejorando el rendimiento.
     - **Escalabilidad**: Capacidad para manejar un creciente número de trabajos, o su capacidad de expandirse para gestionar el crecimiento del trabajo.
   - **Arquitecturas Comunes**:
     - **Cliente-servidor**, **Tres niveles**, **P2P (Peer-to-Peer)**, y **Microservicios**.

#### **Diagrama de Clases en UML**
   - **Propósito**:
     - Representa visualmente la estructura de las clases en un sistema, incluyendo atributos, métodos y relaciones como herencia y asociaciones.
   - **Uso en el Diseño**:
     - Fundamental en OOAD para documentar las relaciones y dependencias entre las clases, lo que facilita la comprensión del diseño del sistema y su implementación.




### Enfoques de la Arquitectura de Aplicaciones

#### **Arquitecturas Basadas en Componentes y Orientada a Servicios**
   - **Componentes**:
     - **Definición**: Unidades de funcionalidad encapsulada dentro de una aplicación.
     - **Características**: Reusabilidad, reemplazo, independencia, extensibilidad, encapsulación, y no específicos del contexto.
     - **Ejemplo**: Una API de conexión a base de datos.

   - **Servicios**:
     - **Definición**: Unidades de funcionalidad diseñadas para ser implementadas de forma independiente y reutilizables en múltiples sistemas.
     - **Diferencia con componentes**: Los servicios tienen una instancia única y siempre en ejecución, a diferencia de los componentes que pueden existir en múltiples instancias.
     - **Ejemplo**: Servicios web que procesan pagos o gestionan credenciales de usuario.

#### **Arquitectura Basada en Componentes**
   - **Enfoque**: Descomposición del diseño en componentes lógicos independientes con acoplamiento flexible.
   - **Ventajas**: Facilita la mantenibilidad y escalabilidad de la aplicación.
   - **Implementación**: Componentes funcionan juntos creando una aplicación integral mediante su interacción definida.

#### **Arquitectura Orientada a Servicios (SOA)**
   - **Definición**: Arquitectura que organiza y utiliza servicios distribuidos y autónomos.
   - **Características**: Los servicios son autónomos, reutilizables y capaces de interactuar a través de una red utilizando un protocolo de comunicación.
   - **Ventajas**: Flexibilidad para integrar diversas aplicaciones y mayor agilidad en adaptarse a cambios o nuevas integraciones.

#### **Sistemas Distribuidos**
   - **Definición**: Sistemas donde los componentes están ubicados en diferentes sistemas de red y comunican entre sí solo mediante mensajes.
   - **Propiedades**: Tolerancia a fallos, concurrencia, escalabilidad, y heterogeneidad.
   - **Arquitecturas comunes**: Cliente-servidor, tres niveles, peer-to-peer (P2P), y microservicios.

#### **Diagramas y Modelado en UML**
   - **Uso de UML**: Permite visualizar la arquitectura, el diseño y la implementación de sistemas de software complejos.
   - **Tipos de Diagramas UML**: Estructurales y conductuales.
   - **Ventajas de UML**: Facilita la planificación, mejora la comunicación dentro del equipo y entre stakeholders, y proporciona una representación visual que ayuda en la navegación y comprensión del sistema.





### Patrones Arquitectónicos en el Software

**Descripción General de los Patrones Arquitectónicos**
   - **Definición**: Soluciones repetibles a problemas comunes en la arquitectura del software.
   - **Propósito**: Facilitar la organización estructural del software, haciendo que el sistema sea más manejable, escalable y comprensible.

**Ejemplos de Patrones Arquitectónicos**

   - **Arquitectura de 2 Niveles (Cliente-Servidor)**
     - **Descripción**: Un servidor gestiona los recursos y servicios, mientras que la interfaz reside en el cliente que solicita esos recursos.
     - **Ejemplo**: Aplicaciones de mensajería donde el servidor maneja el envío de mensajes entre clientes.

   - **Arquitectura de 3 Niveles**
     - **Descripción**: Divide la aplicación en tres capas lógicas: presentación, lógica de negocio (aplicación) y datos.
     - **Ejemplo**: Aplicaciones web que utilizan un servidor web para la interfaz de usuario, un servidor de aplicaciones para la lógica de negocio, y un servidor de bases de datos para la gestión de datos.

   - **Arquitectura Peer-to-Peer (P2P)**
     - **Descripción**: Una red descentralizada donde cada nodo actúa tanto como cliente como servidor.
     - **Ejemplo**: Criptomonedas como Bitcoin, donde cada nodo en la red blockchain actúa como servidor y cliente.

   - **Arquitectura Basada en Eventos**
     - **Descripción**: Se centra en los productores y consumidores de eventos que interactúan mediante un router de eventos.
     - **Ejemplo**: Aplicaciones de servicios de transporte como Uber, donde eventos como solicitudes de viaje son manejados dinámicamente.

   - **Microservicios**
     - **Descripción**: Divide una aplicación en pequeños servicios independientes que comunican a través de API.
     - **Ejemplo**: Redes sociales que utilizan diferentes servicios para gestionar funciones como agregar amigos, recomendaciones y publicaciones.

**Importancia de los Patrones Arquitectónicos**

   - **Flexibilidad**: Facilitan la adaptación a los cambios tecnológicos y a las nuevas exigencias del negocio.
   - **Reusabilidad**: Promueven el uso de componentes que pueden ser reutilizados en diferentes partes del sistema o en diferentes proyectos.
   - **Escalabilidad**: Ayudan a diseñar sistemas que pueden escalarse de manera efectiva para manejar aumentos en la carga de trabajo.
   - **Mantenibilidad**: Mejoran la estructura del software haciéndolo más fácil de entender y mantener.

**Consideraciones de Diseño**

   - **Selección de Patrones**: Depende de los requisitos específicos del proyecto y del entorno en el que se desplegará el sistema.
   - **Combinación de Patrones**: Algunos patrones pueden combinarse para aprovechar las ventajas de cada uno, aunque no todos son compatibles entre sí.




### Entornos de Despliegue de Aplicaciones

**Tipos de Entornos de Preproducción**
   - **Desarrollo**: Donde se realiza la codificación inicial y se hacen las pruebas básicas. Usualmente es el ambiente menos formalizado y está configurado en las estaciones de trabajo de los desarrolladores.
   - **QA (Garantía de Calidad)**: Utilizado para realizar pruebas integrales y asegurar que el software cumpla con los requisitos especificados antes de pasar a producción.
   - **Puesta en escena (Staging)**: Réplica del entorno de producción que se utiliza para realizar pruebas finales y simular cómo funcionará la aplicación en producción.

**Entorno de Producción**
   - **Definición**: Incluye todos los sistemas y recursos necesarios para que la aplicación esté operativa y disponible para el usuario final.
   - **Características**: Alta disponibilidad, escalabilidad, seguridad y manejo de carga elevada. Debe ser robusto y estable para manejar las operaciones diarias de la empresa sin interrupciones.

**Comparación de Entornos**
   - **Diferencias Clave**: Los entornos de preproducción están diseñados para pruebas y no están abiertos al público general. El entorno de producción, en cambio, es donde la aplicación se vuelve accesible a los usuarios finales y donde el rendimiento y la estabilidad son críticos.
   - **Propósito de Preproducción**: Asegurar que todo funcione según lo previsto sin afectar la operación real y los datos de los usuarios.

**Opciones de Implementación**
   - **Implementación Local**: El software y los servidores se encuentran físicamente en las instalaciones de la empresa. Esto ofrece un control completo sobre la infraestructura pero requiere mantenimiento y actualizaciones por parte del personal de la empresa.
   - **Nube Pública**: Utiliza servicios en la nube proporcionados por terceros como AWS, Google Cloud, etc. Ofrece escalabilidad y es generalmente más económico que mantener la infraestructura localmente.
   - **Nube Privada**: Infraestructura dedicada a una sola organización, proporcionando mayor control y seguridad. Puede estar alojada internamente o por un proveedor externo.
   - **Nube Híbrida**: Combina elementos de nubes públicas y privadas, buscando optimizar los beneficios de cada opción según las necesidades específicas de la empresa.

**Consideraciones Clave**
   - **Seguridad**: Especialmente importante en entornos de producción y en cualquier configuración de nube privada donde los datos sensibles deben ser protegidos.
   - **Costo**: La implementación local puede ser más cara a largo plazo, mientras que la nube pública puede ser más asequible pero con menos control.
   - **Escalabilidad**: Las soluciones en la nube ofrecen mejor escalabilidad comparado con los entornos locales, ajustándose mejor a las necesidades cambiantes del negocio.
   - **Mantenimiento y Actualizaciones**: Requieren un enfoque sistemático y cuidadoso para asegurar que los sistemas estén actualizados sin afectar la disponibilidad del servicio.




### Componentes Clave para la Implementación en Producción

**Cortafuegos**
   - **Función**: Supervisa y controla el tráfico de red entrante y saliente basado en reglas de seguridad predeterminadas.
   - **Propósito**: Protege los recursos internos de amenazas externas como virus, malware y ataques cibernéticos, actuando como una barrera entre la red segura interna y las redes no seguras.

**Equilibrador de Carga**
   - **Función**: Distribuye el tráfico de red entrante entre varios servidores para optimizar la utilización de recursos, maximizar el rendimiento, minimizar el tiempo de respuesta y evitar la sobrecarga de cualquier servidor individual.
   - **Propósito**: Asegura la alta disponibilidad y la confiabilidad de las aplicaciones y servicios hospedados, gestionando las solicitudes de manera eficiente y garantizando que ningún servidor se sobrecargue.

**Servidores Web y de Aplicaciones**
   - **Servidor Web**: Maneja las solicitudes HTTP de los clientes, como navegadores web, y les entrega contenido estático y dinámico como páginas web, archivos, imágenes y videos.
   - **Servidor de Aplicaciones**: Gestiona toda la lógica de la aplicación y las interacciones del negocio, proporcionando la funcionalidad necesaria para que las aplicaciones funcionen.

**Servidor Proxy**
   - **Función**: Actúa como intermediario para solicitudes de red de un cliente buscando recursos de otros servidores.
   - **Propósito**: Mejora el rendimiento mediante la caché de contenido, aumenta la seguridad filtrando contenido malicioso y proporciona anonimato para los usuarios.

**Servidor de Base de Datos**
   - **Función**: Almacena y gestiona datos para las aplicaciones mediante un sistema de gestión de bases de datos (DBMS).
   - **Propósito**: Facilita la recuperación eficiente y segura de datos, además de permitir la manipulación de los datos almacenados mediante consultas y transacciones.

### Consideraciones de Implementación

- **Escalabilidad**: Capacidad del entorno para adaptarse a cargas de trabajo incrementadas sin afectar el rendimiento.
- **Seguridad**: Uso de medidas como cortafuegos, encriptación, y autenticación para proteger los datos y las aplicaciones.
- **Rendimiento**: Optimización de recursos y configuración para garantizar tiempos de respuesta rápidos y manejo eficiente del tráfico.
- **Mantenimiento**: Procedimientos para actualizar y gestionar componentes sin interrumpir el servicio.


