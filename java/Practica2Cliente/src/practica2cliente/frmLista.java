/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente;

import javax.swing.JOptionPane;
import practica2cliente.models.ListaResponse;
import practica2cliente.rest.PythonApiClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 *
 * @author estuardoarevalo
 */
public class frmLista extends javax.swing.JFrame {

    PythonApiClient mPythonClient;
    
    /**
     * Creates new form frmLista
     */
    public frmLista() {
        initComponents();
        
        //----------------------------------------------------------------
        // Inicializando el JFrame
        //colocar en el centro de la pantalla
        this.setLocationRelativeTo(null);
        //----------------------------------------------------------------
        
        mPythonClient = new PythonApiClient();
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtAgregar = new javax.swing.JTextField();
        txtBorrar = new javax.swing.JTextField();
        txtBuscar = new javax.swing.JTextField();
        btnAgregar = new javax.swing.JButton();
        btnBorrar = new javax.swing.JButton();
        btnBuscar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        btnAgregar.setText("Agregar");
        btnAgregar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAgregarActionPerformed(evt);
            }
        });

        btnBorrar.setText("Borrar");
        btnBorrar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnBorrarActionPerformed(evt);
            }
        });

        btnBuscar.setText("Buscar");
        btnBuscar.setActionCommand("Buscar");
        btnBuscar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnBuscarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(32, 32, 32)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(txtBuscar, javax.swing.GroupLayout.PREFERRED_SIZE, 261, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(txtBorrar, javax.swing.GroupLayout.PREFERRED_SIZE, 261, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(txtAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 261, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(109, 109, 109)
                        .addComponent(btnAgregar))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(115, 115, 115)
                        .addComponent(btnBorrar))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(116, 116, 116)
                        .addComponent(btnBuscar)))
                .addContainerGap(39, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(txtAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnAgregar)
                .addGap(23, 23, 23)
                .addComponent(txtBorrar, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnBorrar)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 24, Short.MAX_VALUE)
                .addComponent(txtBuscar, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnBuscar)
                .addGap(13, 13, 13))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnAgregarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAgregarActionPerformed
        
        
         mPythonClient.getService().listaAgregar(txtAgregar.getText()).enqueue(new Callback<ListaResponse>() {
        
            @Override
            public void onResponse(Call<ListaResponse> call, Response<ListaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    ListaResponse listaResponse = rspns.body();
                    
                    if (listaResponse.success){
                        JOptionPane.showMessageDialog(null, "Dato ingresado correctamente","Satisfactorio", 
                            JOptionPane.INFORMATION_MESSAGE);
                        txtAgregar.setText("");
                    }else{
                        JOptionPane.showMessageDialog(null, listaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<ListaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llama a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
        
        
    }//GEN-LAST:event_btnAgregarActionPerformed

    private void btnBorrarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnBorrarActionPerformed
        
        mPythonClient.getService().listaEliminar(Integer.parseInt(txtBorrar.getText())).enqueue(new Callback<ListaResponse>() {
        
            @Override
            public void onResponse(Call<ListaResponse> call, Response<ListaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    ListaResponse listaResponse = rspns.body();
                    
                    if (listaResponse.success){
                        JOptionPane.showMessageDialog(null, "Dato Eliminado correctamente","Satisfactorio", 
                            JOptionPane.INFORMATION_MESSAGE);
                        txtAgregar.setText("");
                    }else{
                        JOptionPane.showMessageDialog(null, listaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<ListaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llama a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
    }//GEN-LAST:event_btnBorrarActionPerformed

    private void btnBuscarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnBuscarActionPerformed
        
        mPythonClient.getService().listaBuscar(txtBuscar.getText()).enqueue(new Callback<ListaResponse>() {
        
            @Override
            public void onResponse(Call<ListaResponse> call, Response<ListaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    ListaResponse listaResponse = rspns.body();
                    
                    if (listaResponse.success){
                        
                        if (listaResponse.index>=0){
                        
                            JOptionPane.showMessageDialog(null, "Se encontró el dato en el indice = " + listaResponse.index ,"Satisfactorio", 
                                JOptionPane.INFORMATION_MESSAGE);
                            txtAgregar.setText("");
                        }else{
                            JOptionPane.showMessageDialog(null, "No se encontró el dato", "Error", JOptionPane.ERROR_MESSAGE);
                        }
                    }else{
                        JOptionPane.showMessageDialog(null, listaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<ListaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llama a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
        
    }//GEN-LAST:event_btnBuscarActionPerformed


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAgregar;
    private javax.swing.JButton btnBorrar;
    private javax.swing.JButton btnBuscar;
    private javax.swing.JTextField txtAgregar;
    private javax.swing.JTextField txtBorrar;
    private javax.swing.JTextField txtBuscar;
    // End of variables declaration//GEN-END:variables
}
