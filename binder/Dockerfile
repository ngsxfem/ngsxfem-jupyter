FROM ngsxfem/ngsxfem:latest

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

COPY . ${HOME}

USER root
RUN chown -R ${NB_UID} ${HOME}
RUN pip install jupyter_contrib_nbextensions
RUN pip install jupyter_nbextensions_configurator
RUN pip install RISE
RUN pip install ipywidgets

USER ${NB_USER}

RUN jupyter contrib nbextension install --user
RUN jupyter nbextensions_configurator enable --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable scratchpad/main
RUN jupyter nbextension enable toc2/main
# RUN jupyter nbextension enable varInspector/main
RUN jupyter nbextension enable hide_header/main
RUN jupyter nbextension enable --py widgetsnbextension
WORKDIR /home/${NB_USER}        