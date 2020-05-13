from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        suggestions = {}
        key = ""
        for letter in searchWord:
            key += letter
            suggestions[key] = []

        for product in products:
            productKey = ""
            for letter in product:
                productKey += letter
                if productKey in suggestions:
                    suggestions[productKey].append(product)
                else:
                    break

        productSuggestions = []
        for key in suggestions:
            productSuggestions.append(suggestions[key][:3])

        return productSuggestions


if __name__ == "__main__":
    s = Solution()
    s.suggestedProducts(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags")
