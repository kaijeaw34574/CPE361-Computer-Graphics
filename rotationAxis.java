/* Program to assign a point to create a hexagon around the y-axis from point (x, y, z)
 * 
 * Created Pornthep Sangthongkhamsuk ID: 63070503431
 */

import java.util.*;

public class rotationAxis {

    /* Function to calculate matrix around the y-axis and point (x, y, z) from the user */
    public static void calculate(double x, double y, double z, double[][] array) {
        double[][] point = {{x}, {y}, {z}, {1}};
        double[][] result = new double[4][1];
        /* Calculate the matrix 4*4 and matrix 1*1 */
        for(int i = 0; i < 4; i++) {
            result[i][0] = 0;
            for(int j = 0; j < 4; j++) {
                result[i][0] += array[i][j] * point[j][0];
            }
        }
        /* Show the result to create a hexagon in format point (x, y, z) */
        System.out.format("(%.2f, %.2f, %.2f)" + "\n", result[0][0], result[1][0], result[2][0]);  
    }

    /* Function to set matrix around the y-axis */
    public static void setYaxis(double x, double y, double z) {
        double[][] yaxis = {{60, 0, 60, 0}, {0, 1, 0, 0}, {-60, 0, 60, 0}, {0, 0, 0, 1}};
        double[][] radian = {{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}};
        double[][] array = {{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}};
        for (int i = 0; i <= 5; i++) {
            /* Find an angle from matrix around the y-axis */
            radian[0][0] = Math.toRadians(yaxis[0][0]);
            radian[0][2] = Math.toRadians(yaxis[0][2]);
            radian[2][0] = Math.toRadians(yaxis[2][0]);
            radian[2][2] = Math.toRadians(yaxis[2][2]);

            /* Calculate the value of cos and sin each angle around the y-axis */
            array[0][0] = Math.cos(radian[0][0]);
            array[0][2] = Math.sin(radian[0][2]);
            array[2][0] = Math.sin(radian[2][0]);
            array[2][2] = Math.cos(radian[2][2]);

            calculate(x, y, z, array);
            
            /* Add an angle of 60 in each rotation around the y-axis */
            yaxis[0][0] += 60;
            yaxis[0][2] += 60;
            yaxis[2][0] -= 60;
            yaxis[2][2] += 60;
        }
    }

    /* Main function get the point (x, y, z) from the user */
    public static void main(String[] args) {
        System.out.format("Type 3 points for rotation around the y-axis: "); 
        Scanner sc = new Scanner(System.in); 
        double x = sc.nextDouble(); 
        double y = sc.nextDouble(); 
        double z = sc.nextDouble(); 
        setYaxis(x, y, z);
        sc.close();
    }
}