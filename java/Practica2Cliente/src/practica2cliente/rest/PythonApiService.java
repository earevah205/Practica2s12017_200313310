/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente.rest;

import practica2cliente.models.ColaResponse;
import practica2cliente.models.ListaResponse;
import practica2cliente.models.MatrizResponse;
import practica2cliente.models.PilaResponse;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

/**
 *
 * @author estuardoarevalo
 */
public interface PythonApiService {
    
    @GET("/lista/agregar/{dato}")
    Call<ListaResponse> listaAgregar(@Path("dato") String dato);
    
    @GET("/lista/eliminar/{indice}")
    Call<ListaResponse> listaEliminar(@Path("indice") int indice);
    
    @GET("/lista/buscar/{dato}")
    Call<ListaResponse> listaBuscar(@Path("dato") String dato);
    
    @GET("/lista/graphviz")
    Call<ListaResponse> listaGraphviz();
    
    @GET("/cola/queue/{numero}")
    Call<ColaResponse> colaQueue(@Path("numero") int numero);
    
    @GET("/cola/dequeue")
    Call<ColaResponse> colaDequeue();
    
    @GET("/cola/graphviz")
    Call<ColaResponse> colaGraphviz();
    
    @GET("/pila/push/{numero}")
    Call<PilaResponse> pilaPush(@Path("numero") int numero);
    
    @GET("/pila/pop")
    Call<PilaResponse> pilaPop();
    
    @GET("/pila/graphviz")
    Call<PilaResponse> pilaGraphviz();
    
    @GET("/matriz/agregar/{correo}")
    Call<MatrizResponse> matrizAgregar(@Path("correo") String correo);
    
    @GET("/matriz/borrar/{correo}")
    Call<MatrizResponse> matrizBorrar(@Path("correo") String correo);
    
    @GET("/matriz/buscarDominio/{dominio}")
    Call<MatrizResponse> matrizBuscarDominio(@Path("dominio") String dominio);
    
    @GET("/matriz/buscarLetra/{letra}")
    Call<MatrizResponse> matrizBuscarLetra(@Path("letra") String letra);
    
    @GET("/matriz/graphviz")
    Call<MatrizResponse> matrizGraphviz();
    
}
