/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente;

import java.io.File;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import practica2cliente.models.ColaResponse;
import practica2cliente.models.PilaResponse;
import practica2cliente.rest.PythonApiClient;
import practica2cliente.utils.GraphViz;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 *
 * @author estuardoarevalo
 */
public class frmPila extends javax.swing.JFrame {

    PythonApiClient mPythonClient;
    
    /**
     * Creates new form frmPila
     */
    public frmPila() {
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

        btnPush = new javax.swing.JButton();
        btnPop = new javax.swing.JButton();
        txtPila = new javax.swing.JTextField();
        btnGraphviz = new javax.swing.JButton();

        btnPush.setText("push");
        btnPush.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnPushActionPerformed(evt);
            }
        });

        btnPop.setText("pop");
        btnPop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnPopActionPerformed(evt);
            }
        });

        btnGraphviz.setText("graphviz");
        btnGraphviz.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGraphvizActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(38, 38, 38)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(txtPila, javax.swing.GroupLayout.PREFERRED_SIZE, 313, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(btnPush, javax.swing.GroupLayout.PREFERRED_SIZE, 155, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnPop, javax.swing.GroupLayout.PREFERRED_SIZE, 152, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(49, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(btnGraphviz))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(17, 17, 17)
                .addComponent(txtPila, javax.swing.GroupLayout.PREFERRED_SIZE, 41, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnPush)
                    .addComponent(btnPop))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(btnGraphviz))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnPushActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnPushActionPerformed
        mPythonClient.getService().pilaPush(Integer.parseInt(txtPila.getText())).enqueue(new Callback<PilaResponse>() {
            @Override
            public void onResponse(Call<PilaResponse> call, Response<PilaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    PilaResponse pilaResponse = rspns.body();
                    
                    if (pilaResponse.success){
                        JOptionPane.showMessageDialog(null, "Dato ingresado correctamente","Satisfactorio", 
                            JOptionPane.INFORMATION_MESSAGE);
                        txtPila.setText("");
                        txtPila.requestFocus();
                    }else{
                        JOptionPane.showMessageDialog(null, pilaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<PilaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llamada a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
            
        
            
        });
    }//GEN-LAST:event_btnPushActionPerformed

    private void btnPopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnPopActionPerformed
        mPythonClient.getService().pilaPop().enqueue(new Callback<PilaResponse>() {
            @Override
            public void onResponse(Call<PilaResponse> call, Response<PilaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    PilaResponse pilaResponse = rspns.body();
                    
                    if (pilaResponse.success){
                        
                        if (pilaResponse.numero != 0)
                        {
                            JOptionPane.showMessageDialog(null, "Sale de la pila el dato " + pilaResponse.numero,"Satisfactorio", 
                                JOptionPane.INFORMATION_MESSAGE);
                        }else{
                            JOptionPane.showMessageDialog(null, "La pila está vacía", "Error", JOptionPane.ERROR_MESSAGE);
                        }
                    }else{
                        JOptionPane.showMessageDialog(null, pilaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<PilaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llamada a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
            
            
        });
    }//GEN-LAST:event_btnPopActionPerformed

    private void btnGraphvizActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGraphvizActionPerformed

        
        mPythonClient.getService().pilaGraphviz().enqueue(new Callback<PilaResponse>() {
            @Override
            public void onResponse(Call<PilaResponse> call, Response<PilaResponse> rspns) {
                if (rspns.isSuccessful()) {
                    PilaResponse pilaResponse = rspns.body();
                    
                    if (pilaResponse.success){
                        
                        GraphViz gv = new GraphViz();
                        gv.addln(gv.start_graph());

                        gv.add(pilaResponse.graphviz);

                        gv.addln(gv.end_graph());

                        System.out.println(gv.getDotSource());
                        gv.decreaseDpi();   // 106 dpi
                        String type = "gif";
                        String repesentationType= "dot";
                        String imagePath = gv.getTempDir() + "/lista"+GraphViz.now()+gv.getImageDpi()+"."+ type;
                        File out = new File( imagePath );
                        gv.writeGraphToFile( gv.getGraph(gv.getDotSource(), type, repesentationType), out );

                        //creamos el objeto graphviz
                        //String imagePath = colaDeFichas.crearImagenGraphviz();
                        System.out.println(imagePath);
                        mostrarPanelGraphviz(imagePath);
                        
                    }else{
                        JOptionPane.showMessageDialog(null, pilaResponse.error, "Error", JOptionPane.ERROR_MESSAGE);
                    }
                    
                } else {
                    JOptionPane.showMessageDialog(null, "Ocurrió un Error" + "Code: " 
                            + rspns.code() + "Message: " 
                            + rspns.message(), "Error", 
                            JOptionPane.ERROR_MESSAGE);
                }
            }

            @Override
            public void onFailure(Call<PilaResponse> call, Throwable thrwbl) {
                JOptionPane.showMessageDialog(null, "Error en Llamada a python", "Error", JOptionPane.ERROR_MESSAGE);
            }
            
            
        });
        
    }//GEN-LAST:event_btnGraphvizActionPerformed

    private void mostrarPanelGraphviz(String imagePath){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frmGraph it = new frmGraph(imagePath);
        frame.add(it);
        frame.pack();
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
        
    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnGraphviz;
    private javax.swing.JButton btnPop;
    private javax.swing.JButton btnPush;
    private javax.swing.JTextField txtPila;
    // End of variables declaration//GEN-END:variables
}
