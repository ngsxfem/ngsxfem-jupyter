FROM ngsxfem/ngsxfem:v2.0.2105

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

# RUN pip3 install --no-cache-dir notebook==5.*
        
COPY . ${HOME}

USER root
ENV TINI_VERSION v0.6.0 
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini 
RUN chmod +x /usr/bin/tini 

RUN chown -R ${NB_UID} ${HOME}

RUN pip3 install jupyter_contrib_nbextensions
RUN pip3 install jupyter_nbextensions_configurator
RUN pip3 install RISE
RUN pip3 install ipywidgets

USER ${NB_USER}

WORKDIR /home/${NB_USER}

RUN jupyter contrib nbextension install --user
RUN jupyter nbextensions_configurator enable --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable scratchpad/main
RUN jupyter nbextension enable toc2/main
# RUN jupyter nbextension enable varInspector/main
RUN jupyter nbextension enable hide_header/main
RUN jupyter nbextension enable --py widgetsnbextension


ENTRYPOINT ["/usr/bin/tini", "--"] 

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root" ]      