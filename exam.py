// muruj haddad
// 444001151
// I changed the attribute name 
//----------------------------------------------------------------------------------------------

// Java code for linearly search x in arr[]. If h

// is present then return its location, otherwise

// return -1

class LinearSearch {

            // This function returns index of element x in arr[]

            static int search(int arr[], int m, int h)

            {

                        for (int i = 0; i < m; i++) {

                                // Return the index of the element if the element

                                    // is found

                                    if (arr[i] == h)

                                                return i;

                        }
 

                        // return -1 if the element is not found

                        return -1;

            }

 

            public static void main(String[] args)

            {

                        int[] arr = { 3, 4, 1, 7, 5 };

                        int h = arr.length;

                        int m = 4;

                        int index = search(arr, m, h);

                        if (index == -1)

                          System.out.println("Element is not present in the array");
                        else

                          System.out.println("Element found at position " + index);

            }

}

//------------------------------------------------------------------------------------------------------

