import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {
    public static String getMd5(String input) {
        try {
            // Create an instance of MessageDigest with MD5 algorithm
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Calculate the message digest of the input
            byte[] messageDigest = md.digest(input.getBytes());

            // Convert byte array to signum representation
            BigInteger no = new BigInteger(1, messageDigest);

            // Convert message digest to hex value
            String hashText = no.toString(16);

            // Pad the hashText with leading zeros if necessary
            while (hashText.length() < 32) {
                hashText = "0" + hashText;
            }

            return hashText;
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        String input = "I AM AS CALM AS CLOUDS";
        String md5Hash = getMd5(input);
        System.out.println("Your HashCode Generated by MD5 is: " + md5Hash);
    }
}