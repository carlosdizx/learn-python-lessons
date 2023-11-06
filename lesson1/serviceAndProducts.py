customer_satisfied_product = {101, 102, 103, 104, 105}
customer_service_satisfaction = {103, 104, 105, 106, 107}
recommended_product = {101, 103, 105, 107, 108}
negative_feedback = {102, 106, 108}

customer_both_satisfaction = customer_satisfied_product.intersection(customer_service_satisfaction)
print("Clientes satisfechos con el producto y con el servicio", customer_both_satisfaction)

customer_satisfaction = customer_satisfied_product.union(customer_service_satisfaction)
print("Clientes satisfechos con el producto y con el servicio", customer_satisfaction)

customer_recommended_product_and_negative_feedback = recommended_product.intersection(negative_feedback)
print("Clientes que han recomendado el producto y tienen reseña negativa",
      customer_recommended_product_and_negative_feedback)

customer_dissatisfied_product = customer_satisfied_product.symmetric_difference(
    customer_service_satisfaction.union(recommended_product.union(negative_feedback)))
print("Clientes que insatisfechos con el producto", customer_dissatisfied_product)

customer_without_recommended_service = negative_feedback.difference(customer_service_satisfaction)
print("Clientes que no han Dado retroalimentación negativa sobre el servicio al cliente",
      customer_without_recommended_service)
