/***************************************************************************
 *  AVR Test for Toolchain on Arch Linux
 *  
 *
 *  Created: 2021-04-15
 *  Updated: 2021-04-15
 *  Author: nlantau
 **************************************************************************/

/***** Include guard ******************************************************/

#ifndef F_CPU
#define F_CPU 16000000UL
#endif /* F_CPU */

/***** Include section ****************************************************/

#include <avr/io.h>
#include <stdlib.h>
#include <util/delay.h>

/***** Macro Definitions **************************************************/

/***** Function prototypes ************************************************/

/***** Constants **********************************************************/

/***** MAIN ***************************************************************/

int main(void)
{
    DDRD |= 0xFF;

    while (1)
    {
    PORTD |= (1 << PIND1);
    PORTD |= (1 << PIND2);
    //PORTD |= (1 << PIND3);
    PORTD |= (1 << PIND4);


    PORTD &= ~(1 << PIND1);
    PORTD &= ~(1 << PIND2);
    PORTD &= ~(1 << PIND3);
    PORTD &= ~(1 << PIND4);
        
    }
}

