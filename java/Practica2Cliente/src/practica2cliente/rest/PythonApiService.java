/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente.rest;

import practica2cliente.models.ListaResponse;
import retrofit2.Call;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
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
}
