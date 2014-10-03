/**
 * Created by chelck on 1/5/14.
 */

object Problem999 extends Problem(1234L) {

  override def apply(): Long = Totient.phi(999)
}



