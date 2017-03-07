/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2cliente.utils;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author estuardoarevalo
 */
public class ValidatorUtil {
    private static final String PATTERN_EMAIL = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
            + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$";
 
    private static final String PATTERN_LETTER = "^[A-Za-z]$";
 
    private static final String PATTERN_DOMAIN = "^[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$";
 
    /**
     * Validate given email with regular expression.
     * 
     * @param email
     *            email for validation
     * @return true valid email, otherwise false
     */
    public static boolean validateEmail(String email) {
 
        // Compiles the given regular expression into a pattern.
        Pattern pattern = Pattern.compile(PATTERN_EMAIL);
 
        // Match the given input against this pattern
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
 
    }
    
    public static boolean validateLetter(String letter) {
 
        // Compiles the given regular expression into a pattern.
        Pattern pattern = Pattern.compile(PATTERN_LETTER);
 
        // Match the given input against this pattern
        Matcher matcher = pattern.matcher(letter);
        return matcher.matches();
 
    }
    
    public static boolean validateDomain(String domain) {
 
        // Compiles the given regular expression into a pattern.
        Pattern pattern = Pattern.compile(PATTERN_DOMAIN);
 
        // Match the given input against this pattern
        Matcher matcher = pattern.matcher(domain);
        return matcher.matches();
 
    }
}
