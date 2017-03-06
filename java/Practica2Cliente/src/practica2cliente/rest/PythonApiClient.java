/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente.rest;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 *
 * @author estuardoarevalo
 */
public class PythonApiClient {
    private static final String BASE_URL = "http://127.0.0.1:5000/";
    private PythonApiService mPythonApiService;

    public PythonApiClient(){

        String baseUrl = BASE_URL;

        Retrofit retrofit = new Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build();

        mPythonApiService = retrofit.create(PythonApiService.class);

    }
    public PythonApiService getService()
    {
        return mPythonApiService;
    }
}
